# Ngrok A Directory
# 
# Serves the default share diretory and 
# opens the finder to the folder

# TODO: Open a local web page that's generated to 
# provide links to all the files so you can copy
# and paste them that way (instead of letting)
# the full directory be browsed. 

function ngs () {
  SHARE_DIR=/Users/alan/_web_share_tmp
  open $SHARE_DIR
  ngrok http -bind-tls=true "file://$SHARE_DIR"
}
