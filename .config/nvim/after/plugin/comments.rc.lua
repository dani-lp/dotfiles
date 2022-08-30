local status, comments = pcall(require, 'Comment')
if (not status) then return end

comments.setup {}
