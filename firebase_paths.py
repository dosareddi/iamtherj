# A channel is of the form /channels/12134572323
# where the path is the name of the channel.
CHANNELS_PATH = "/channels"

# Channel Info is of the form /channels/12134572323/info
CHANNELS_INFO_SUBDIR = "/info"
CHANNELS_INFO_KEY_STATE = "state"
CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED = 0
CHANNELS_INFO_VAL_STATE_WAITING_FOR_WORKER = 1
CHANNELS_INFO_VAL_STATE_WAITING_FOR_CUSTOMER = 2

# Channel Worker ID is a mapping of the form /channel_worker
# A key is a channel id and value is worker id if any assigned, if none then
# value is 0.
CHANNEL_WORKER_PATH = "/channel_worker"

# This is used for mapping a slack channel id to channel name.
SLACK_ID_CHANNEL_NAME_PATH = "/slack_id/channel"

# A worker path of the form /workers/<slack_id>
WORKERS_PATH = "/workers"
WORKERS_KEY_NAME = "name"



