<template>
    <div>
        <div class="col-md-12" v-show="todos.length>0">
            <h3>Auction Hunter</h3>
            <div class="row mrb-10" v-for="todo in todos">
                <div class="input-group m-b-5">
                    <p>{{todo.car_name}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import bus from './../bus.js'

    export default {
        data() {
            return {
                todos: []
            }
        },
        created: function() { // get todo items and start listening to events once component is created
            this.fetchTodo();
            this.listenToEvents();
        },
        methods: {
            fetchTodo() {
                let uri = 'http://localhost:8080/api/all';
                axios.get(uri).then((response) => {
                    this.todos = response.data;
                });
            },
            listenToEvents() {
                bus.$on('refreshTodo', ($event) => {
                    this.fetchTodo(); // referesh or update todo list on the page
                })
            }
        }
    }
</script>
<style scoped>
    .delete__icon {}
    .todo__done {
        text-decoration: line-through !important
    }
    .no_border_left_right {
        border-left: 0px;
        border-right: 0px;
    }
    .flat_form {
        border-radius: 0px;
    }
    .mrb-10 {
        margin-bottom: 10px;
    }
    .addon-left {
        background-color: none !important;
        border-left: 0px !important;
        cursor: pointer !important;
    }
    .addon-right {
        background-color: none !important;
        border-right: 0px !important;
    }
</style>
