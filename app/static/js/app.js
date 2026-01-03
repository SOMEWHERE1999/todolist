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

    vm.loadTodos = function () {
      TodoService.list().then((response) => {
        vm.todos = (response.data.data || []).map((item) => ({
          ...item,
          isDone: item.status === 'completed',
          isEditing: false,
          editTitle: item.title,
        }));
      });
    };

    vm.addTodo = function () {
      if (!vm.newTitle) return;
      const payload = { title: vm.newTitle.trim(), status: 'pending' };
      if (!payload.title) return;

      TodoService.create(payload).then(() => {
        vm.newTitle = '';
        vm.loadTodos();
      });
    };

    vm.toggleDone = function (todo) {
      const status = todo.isDone ? 'completed' : 'pending';
      todo.status = status;
      TodoService.update(todo.id, { status }).then(() => {
        todo.isDone = status === 'completed';
      });
    };

    vm.startEdit = function (todo) {
      todo.isEditing = true;
      todo.editTitle = todo.title;
    };

    vm.cancelEdit = function (todo) {
      todo.isEditing = false;
      todo.editTitle = todo.title;
    };

    vm.saveEdit = function (todo) {
      const updatedTitle = (todo.editTitle || '').trim();
      if (!updatedTitle) {
        todo.editTitle = todo.title;
        todo.isEditing = false;
        return;
      }

      TodoService.update(todo.id, { title: updatedTitle }).then(() => {
        todo.title = updatedTitle;
        todo.isEditing = false;
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
