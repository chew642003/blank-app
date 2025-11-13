import streamlit as st
import clips
import logging

logging.basicConfig(level=15,format='%(message)s')

env = clips.Environment()
try:
    # clipspy exposes a `LoggingRouter` class (capital L). Older examples
    # may use a different name; guard against that and continue if absent.
    router = clips.LoggingRouter()
    env.add_router(router)
except AttributeError:
    logging.warning('clips.LoggingRouter not available; continuing without router')

name = st.text_input("Enter your name")

env.build("(deftemplate result (slot name))")
env.assert_string(f'(result(name "{name}"))')
env.run()

results = []
for fact in env.facts():
    if fact.template.name == 'result' :
        results.append(fact['name'])

st.write(results[0],"output")