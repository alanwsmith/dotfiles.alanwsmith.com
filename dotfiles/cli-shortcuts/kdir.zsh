function kdir () {
  KSUID=`/Users/alan/go/bin/ksuid | tr '[:upper:]' '[:lower:]'`
  DIRSTRING=`printf '%s_%.12s' $1 $KSUID`
  mkdir "$DIRSTRING"
}

