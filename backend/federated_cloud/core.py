import json

import requests

from federated_cloud.models import CMSCache, SiteCache


def send_federated_cloud_request(domain, tail):
    return requests.get(domain + "/federated-cloud/" + tail)


def ask_for_cms_ids(domain):
    response = send_federated_cloud_request(domain, "cms-ids")
    response_list = json.loads(response.text)
    return response_list


def ask_for_cms_data(domain, cms_id):
    response = send_federated_cloud_request(domain, "cms-data/" + str(cms_id))
    response_dict = json.loads(response)
    response_cms = CMSCache(
        id=cms_id,
        name=response_dict["name"],
        domain=response_dict["domain"],
        public_key=response_dict["public_key"],
        useSites=True,
        askForCMSs=True,
        shareWithOthers=True
    )
    response_cms.save()


def ask_for_site_data(cms_cache):
    response = send_federated_cloud_request(cms_cache.domain, "site-data")
    response_list = json.loads(response)
    for responseElement in response_list:
        SiteCache(
            parentCMS=cms_cache,
            path=responseElement["path"],
            postal_code=responseElement["postal_code"],
            prefix=responseElement["prefix"],
            name_without_prefix=responseElement["name_without_prefix"],
            aliases=responseElement["aliases"],
            latitude=responseElement["latitude"],
            longitude=responseElement["longitude"],
        ).save()


def send_offer():
    pass

# todo error-handling
