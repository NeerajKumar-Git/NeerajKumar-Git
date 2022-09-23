def lowest_common_ancestor(root,p,q):
    if root is None: return None
    if root in [p,q]:
        return root
    leftsub = lowest_common_ancestor(root.left,p,q)
    rightsub = lowest_common_ancestor(root.right,p,q)
    
    if leftsub is None and rightsub is None:
        return None
    if leftsub is None:
        return rightsub
    if rightsub is None:
        return leftsub
    return root
