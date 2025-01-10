import streamlit as st
import mymodule as functions


todos = functions.get_todos()

def add_todo():
    newtodo = st.session_state['new_todo'] + "\n"
    todos.append(newtodo)
    functions.write_todos(todos)


st.title("My To-Do app")
st.write("This app is to increase my productivity. feel free to add todos")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        


st.text_input(label=" ",placeholder="Enter a Todo Item", on_change=add_todo, key="new_todo")

# st.write(st.session_state)