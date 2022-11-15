function watch () {
    fswatch -event UPDATE -0 "$1" | xargs -0 -n1 cat
}
