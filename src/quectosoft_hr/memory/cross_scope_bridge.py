class CrossScopeBridge:
    def promote(self, item, from_scope, to_scope):
        promoted = dict(item)
        promoted["from_scope"] = from_scope
        promoted["to_scope"] = to_scope
        return promoted
