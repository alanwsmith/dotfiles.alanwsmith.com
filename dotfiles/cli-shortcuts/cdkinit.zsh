function cdkinit () {
  if $(type deactivate &> /dev/null 2>&1) 
  then
    deactivate
  fi
  cdk init app --language python && \
  rm -rf .venv && \
  python3 -m venv venv && \
  source venv/bin/activate && \
  python -m pip install -r requirements.txt && \
  echo "venv" >> .gitignore && \
  source venv/bin/activate && \
  rm source.bat && \
  rm README.md && \
  touch README.md
}

