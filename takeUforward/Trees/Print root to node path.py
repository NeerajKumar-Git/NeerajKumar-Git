def roottonode(root,value):
    if root is None:
        return []
    if root.data == value:
        return [value]
    
    lefttree = roottonode(root.left,value)
    righttree = roottonode(root.right,value)
    if lefttree==[] and righttree==[]:
        return []
    if lefttree == []:
        return [root.data]+righttree
    return [root.data]+lefttree
