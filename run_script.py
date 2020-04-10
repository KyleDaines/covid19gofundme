#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

# regular imports
from api.models import Campaign
import json


# main script
def main():

    Campaign.objects.all().delete()

    # read JSON file
    with open('campaign2.json') as json_file:
        data=json.load(json_file)
    campaigns = data['campaign']
    # loop through JSON
        # create products
    for camp in campaigns:
        dbcamp = Campaign()
        dbcamp.campaign_id = camp['campaign_id']
        dbcamp.url = camp['url']
        dbcamp.auto_fb_post_mode = camp['auto_fb_post_mode']
        dbcamp.collected_date = camp['collected_date']
        dbcamp.category_id = camp['category_id']
        dbcamp.category = camp['category']
        dbcamp.currencycode = camp['currencycode']
        dbcamp.current_amount = camp['current_amount']
        dbcamp.goal = camp['goal']
        dbcamp.donators = camp['donators']
        dbcamp.days_active = camp['days_active']
        dbcamp.days_created = camp['days_created']
        dbcamp.title = camp['title']
        dbcamp.description = camp['description']
        dbcamp.default_url = camp['default_url']
        dbcamp.has_beneficiary = camp['has_beneficiary']
        dbcamp.media_type = camp['media_type']
        dbcamp.project_type = camp['project_type']
        dbcamp.turn_off_donations = camp['turn_off_donations']
        dbcamp.user_id = camp['user_id']
        dbcamp.user_first_name = camp['user_first_name']
        dbcamp.user_last_name = camp['user_last_name']
        dbcamp.user_facebook_id = camp['user_facebook_id']
        dbcamp.user_profile_url = camp['user_profile_url']
        dbcamp.visible_in_search = camp['visible_in_search']
        dbcamp.status = camp['status']
        dbcamp.deactivated = camp['deactivated']
        dbcamp.state = camp['state']
        dbcamp.is_launched = camp['is_launched']
        dbcamp.campaign_image_url = camp['campaign_image_url']
        dbcamp.created_at = camp['created_at']
        dbcamp.launch_date = camp['launch_date']
        dbcamp.campaign_hearts = camp['campaign_hearts']
        dbcamp.social_share_total = camp['social_share_total']
        dbcamp.social_share_last_update = camp['social_share_last_update']
        dbcamp.location_city = camp['location_city']
        dbcamp.location_country = camp['location_country']
        dbcamp.location_zip = camp['location_zip']
        dbcamp.is_charity = camp['is_charity']
        dbcamp.charity_valid = camp['charity_valid']
        dbcamp.charity_npo_id = camp['charity_npo_id']
        dbcamp.charity_name = camp['charity_name']
        dbcamp.velocity = camp['velocity']
        dbcamp.average_amount = camp['average_amount']
        dbcamp.quality = camp['quality']

        dbcamp.save()
    
    

# bootstrap
if __name__ == '__main__':
    main()
