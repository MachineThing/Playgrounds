-- Seeing if there is recursion in Lua

function recursion()
  print('recursion')
  recursion()
end

recursion() -- Lua supports recursion
