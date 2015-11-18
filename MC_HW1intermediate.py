##Author: AE

#New research question: To what extent did main stream news media pick up on the recent Spooky Action at a Distance result?
#How many sentences, among the sources that mediacloud pulls from, include the three main terms together (spooky, action, distance)?
#Time frame given is all time (currently less than 1 month) past the publication date in Nature (Oct 21st 2015).

import mediacloud, datetime

API_File = open('MC_ApiKey.txt','r')
API_KEY = API_File.read()

mc = mediacloud.api.MediaCloud(API_KEY)

res = mc.sentenceCount('(spooky AND action AND distance)', solr_filter=[mc.publish_date_query( datetime.date( 2015, 10, 20), datetime.date( 2015, 11, 18) ), 'media_sets_id:1' ])


print "Count of (spooky AND action AND distance) occurences:", res['count'] #prints count of sentences that reference (spooky, action, distance)

    
#ran successfully. Count of (spooky AND action AND distance) occurences: 24

