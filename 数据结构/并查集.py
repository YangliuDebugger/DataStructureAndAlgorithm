# 参考: https://oi-wiki.org/ds/dsu/


fa = {}  # 记录祖先


# 初始化每个node的祖先都是自己
def makeSet(size):
    for i in range(0, size):
        fa[i] = i
    return


# 带路径压缩的祖先寻找
def find(x):
    if x != fa[x]: # x 不是自身的父亲，即 x 不是该集合的代表
        fa[x] = find(fa[x]) # 查找 x 的祖先直到找到代表，于是顺手路径压缩
    return fa[x]


# 启发式合并，当合并两个家族的时候，让总子节点少的祖先的父亲为总子节点多的祖先
# size = [1] * N # 记录并初始化子树的大小为 1
def unionSet(x, y, size):
    xx = find(x)
    yy = find(y)
    if xx == yy:
        return
    if size[xx] > size[yy]: # 保证小的合到大的里
        xx, yy = yy, xx
    fa[xx] = yy
    size[yy] = size[yy] + size[xx]