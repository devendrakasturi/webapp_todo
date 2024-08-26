import streamlit as st
import functions

st.title("To do app")
st.header("Plan efficiently")

todos = functions.get_todos(filepath="files/todos.txt")

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    functions.write_todos(filepath="files/todos.txt", todos_local=todos)
    print(new_todo)


for index, todo in enumerate(todos):
    if not todo == "\n":
        checkbox = st.checkbox(label=todo, key =todo)


st.text_input(label="Enter new todo", placeholder="new todo", key="new_todo", on_change=add_todo)


def remove_todo():
    for todo in todos:
        if st.session_state[todo] == True:
            todos.remove(todo)
    functions.write_todos(filepath="files/todos.txt", todos_local=todos)


st.button(label="Remove", key="remove", type="primary", on_click=remove_todo)
st.button(label="Edit", type="primary")
