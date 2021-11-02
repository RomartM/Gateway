from django.urls import reverse_lazy

from Gateway.system_meta import APP_VERSION, APP_VERSION_LINK, DEVELOPER_LINK, \
 DOCUMENTATION_LINK


def app_meta(request):
    return {
        'APP_VERSION': APP_VERSION,
        'APP_VERSION_LINK': APP_VERSION_LINK,
        'DEVELOPER_LINK': DEVELOPER_LINK,
        'INSTITUTION_NAME': '',
        'TERMS_AND_CONDITION_LINK': reverse_lazy('feedback:terms_and_conditions'),
        'PRIVACY_POLICY_LINK': reverse_lazy('feedback:privacy_policy'),
        'DOCUMENTATION_LINK': DOCUMENTATION_LINK,
        'COPYRIGHT_LABEL': '<a href="%s" class="link-secondary">%s</a>. All rights reserved'
    }