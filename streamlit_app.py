import streamlit as st
import clips
import logging

logging.basicConfig(level=15,format='%(message)s')

env = clips.Environment()
router = clips.loggingRouter()
env.add_router(router)


name = st.text_input("Enter your name")

env.build("(deftemplate result (slot name))")
env.assert_string(f'(result(name "{name}"))')
env.run()

results = []
for fact in env.facts():
    if fact.template.name == 'result' :
        results.append(fact['name'])

st.write(results[0],"output")