import streamlit as st

#Todo functions
def get_todos(filepath=f'Todos/todos.txt'):
    """ Read the text file and return list of contents
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(contents_local, filepath=f'Todos/todos.txt'):
    """overwrites existing file to write the whole list in it now
    store list items in text file
    opens text file in write mode and creates file objet representing the opened file
    """

    with open(filepath, 'w') as file_local:
        file_local.writelines(contents_local) #write new list to file           
    
    #Doesn't return anything since this file is a procedure that just modifies the file

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    set_todos(todos)

st.header("To-do list app")
st.write("Welcome to the to-do list app, which is used to create and complete tasks. I have created a web app, desktop app, and command line version of this application. This was created during the Python course taught by Andrew Sulce.")

st.divider()

st.subheader("Web app version")

todos = get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        set_todos(todos) #write updated list
        del st.session_state[todo] #remove it from the dictionary
        st.experimental_rerun()

st.text_input(label="Enter a todo", 
              placeholder="Buy groceries",
              on_change = add_todo, key='new_todo')

st.divider()

st.subheader("Desktop App Version")

st.image('TodoGUI.png')

st.link_button(label='Github Desktop App', url='https://github.com/HebaAz/TodoApp/blob/main/TodoApp/gui.py')
