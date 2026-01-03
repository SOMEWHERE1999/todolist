(function () {
  'use strict';

  angular
    .module('todoApp', [])
    .factory('TodoService', TodoService)
    .controller('TodoController', TodoController);

  TodoService.$inject = ['$http'];
  function TodoService($http) {
    const API_BASE = '/api/todos';
    return {
      list: () => $http.get(`${API_BASE}/`),
      create: (payload) => $http.post(`${API_BASE}/`, payload),
      update: (id, payload) => $http.put(`${API_BASE}/${id}`, payload),
      remove: (id) => $http.delete(`${API_BASE}/${id}`),
    };
  }

  TodoController.$inject = ['TodoService'];
  function TodoController(TodoService) {
    const vm = this;
    vm.todos = [];
    vm.newTitle = '';
    vm.newDueDate = '';

    vm.loadTodos = function () {
      TodoService.list().then((response) => {
        vm.todos = response.data.data || [];
      });
    };

    vm.addTodo = function () {
      if (!vm.newTitle) return;
      const payload = { title: vm.newTitle, status: 'pending' };
      if (vm.newDueDate) {
        payload.due_date = vm.newDueDate;
      }
      TodoService.create(payload).then(() => {
        vm.newTitle = '';
        vm.newDueDate = '';
        vm.loadTodos();
      });
    };

    vm.updateTodo = function (todo) {
      TodoService.update(todo.id, {
        title: todo.title,
        status: todo.status,
        due_date: todo.due_date,
      });
    };

    vm.removeTodo = function (todo) {
      TodoService.remove(todo.id).then(() => {
        vm.todos = vm.todos.filter((item) => item.id !== todo.id);
      });
    };

    vm.loadTodos();
  }
})();
