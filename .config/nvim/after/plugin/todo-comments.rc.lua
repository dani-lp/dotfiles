local status, todo = pcall(require, 'todo-comments')
if (not status) then return end

todo.setup {}
