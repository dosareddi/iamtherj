# A channel is of the form /channels/12134572323
# where the path is the name of the channel.
CHANNELS_PATH = "/channels"

# Used to keep track of the timestamp of the last fwded message from a channel
CHANNELS_LAST_FWD_TIME = "/channels_last_fwd_time"

# Channel Worker ID is a mapping of the form /channel_worker
# A key is a channel id and value is worker id if any assigned, if none then
# value is 0.
CHANNEL_WORKER_PATH = "/channel_worker"

# This is used for mapping a slack channel id to channel name.
SLACK_ID_CHANNEL_NAME_PATH = "/slack_id/channel"

# This is used for mapping a slack channel id to channel name.
CHANNEL_NAME_SLACK_ID_PATH = "/channel_slack_id"

# A worker path of the form /workers/<slack_id>
WORKERS_PATH = "/workers"
WORKERS_KEY_NAME = "name"



