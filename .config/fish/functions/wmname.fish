function wmname
  xprop | grep WM_CLASS | awk '{print $4}'
end
