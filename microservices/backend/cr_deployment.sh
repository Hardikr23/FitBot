# Set your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="gen-lang-client-0353594207"

# Set your desired Google Cloud Location
export GOOGLE_CLOUD_LOCATION="europe-west2" # Example location

# Set the path to your agent code directory
export AGENT_PATH="./src" # Assuming capital_agent is in the current directory

# Set a name for your Cloud Run service (optional)
export SERVICE_NAME="sports-doctor"

# Set an application name (optional)
export APP_NAME="src"

adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH