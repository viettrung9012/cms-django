from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.shortcuts import render

from .language_form import LanguageForm
from ...models import Language
from ...decorators import staff_required


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_required, name='dispatch')
class LanguageListView(PermissionRequiredMixin, TemplateView):
    permission_required = 'cms.manage_languages'
    raise_exception = True

    template_name = 'languages/list.html'
    base_context = {'current_menu_item': 'languages'}

    def get(self, request, *args, **kwargs):
        languages = Language.objects.all()

        return render(
            request,
            self.template_name,
            {
                **self.base_context,
                'languages': languages
            }
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_required, name='dispatch')
class LanguageView(PermissionRequiredMixin, TemplateView):
    permission_required = 'cms.manage_languages'
    raise_exception = True

    template_name = 'languages/language.html'
    base_context = {'current_menu_item': 'languages'}

    def get(self, request, *args, **kwargs):
        language_code = self.kwargs.get('language_code', None)
        language = Language.objects.filter(code=language_code).first()
        form = LanguageForm(instance=language)
        return render(request, self.template_name, {
            'form': form, **self.base_context
        })

    def post(self, request, *args, **kwargs):
        language_code = self.kwargs.get('language_code', None)
        language = Language.objects.filter(code=language_code).first()
        form = LanguageForm(
            request.POST,
            instance=language
        )
        if form.is_valid():
            form.save()
            if language_code:
                messages.success(request, _('Language saved successfully.'))
            else:
                messages.success(request, _('Language created successfully'))
        else:
            # TODO: error handling
            # TODO: improve messages
            messages.error(request, _('An error has occurred.'))

        return render(request, self.template_name, {
            'form': form, **self.base_context
        })
