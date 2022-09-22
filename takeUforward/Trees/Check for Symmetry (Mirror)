def check_symmetric(root):
    def issymmetric(a,b):
        if a is None or b is None:
            return a==b
        if a.data != b.data:
            return False
        small1 = issymmetric(a.left,b.right)
        small2 = issymmetric(a.right,b.left)
        if small1 and small2:
            return True
        return False
    
    return issymmetric(root.left,root.right)
