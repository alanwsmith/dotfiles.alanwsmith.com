You can use this to figure out what the 
app names are for open apps:

```bash
yabai -m query --windows | jq '.[] | { app: .app, title: .title }'
```

