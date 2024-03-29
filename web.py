import streamlit as st
#streamlit is used easy to create web apps,very intuitive to use,integrates very well with graphs.
import functions




# Your app code goes here

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My web app")
st.subheader("This is my to-do app.")


for index,todo in  enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label=" ",placeholder="add new todo",
              on_change=add_todo,key="new_todo")


#session.state is dictionary type object that displays widgets.