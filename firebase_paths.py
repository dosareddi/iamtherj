
# A channel is of the form /channels/12134572323
# where the path is the name of the channel.
CHANNELS_PATH = "/channels"

# Channel Info is of the form /channels/12134572323/info
CHANNELS_INFO_SUBDIR = "/info"
CHANNELS_INFO_KEY_STATE = "state"
CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED = 0
CHANNELS_INFO_VAL_STATE_WAITING_FOR_WORKER = 1
CHANNELS_INFO_VAL_STATE_WAITING_FOR_CUSTOMER = 2

# Channel Worker Info is of the form /channels/12134572323/worker_info
CHANNELS_WORKERINFO_SUBDIR = "/worker_info"
CHANNELS_WORKERINFO_KEY_ID = "id"
CHANNELS_WORKERINFO_KEY_LAST_WORKER_REQUEST_TS = "last_worker_request_ts"

# Channel Message Info is of the form /channels/12134572323/message_info
CHANNELS_MESSAGEINFO_SUBDIR = "/message_info"
CHANNELS_MESSAGEINFO_KEY_LAST_SENT_TS = "last_sent_ts"

# This is used for mapping a slack channel id to channel name.
SLACK_ID_CHANNEL_NAME_PATH = "/slack_id/channel"

# A worker path of the form /workers/<slack_name>
WORKERS_PATH = "/workers"
# Slack id is stored here.
WORKERS_KEY_ID = "id"
WORKERS_KEY_NAME = "name"
