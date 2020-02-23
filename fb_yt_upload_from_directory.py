import os
import facebook

# FACEBOOK VIDEO UPLOAD
# =====================
# no video upload yet https://github.com/mobolic/facebook-sdk/issues/265
# https://developers.facebook.com/docs/graph-api/reference/page/videos/

# FACEBOO API EXPLORER
# https://developers.facebook.com/tools/explorer/

graph = facebook.GraphAPI(
    access_token=os.environ['FB_TOKEN'],
    version='6.0',
)

# https://developers.google.com/youtube/v3/guides/uploading_a_video
