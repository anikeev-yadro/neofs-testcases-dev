EACL_OBJ_FILTERS = {'$Object:objectID': 'ID',
                    '$Object:containerID': 'CID',
                    '$Object:ownerID': 'OwnerID',
                    '$Object:creationEpoch': 'creationEpoch',
                    '$Object:payloadLength': 'payloadLength',
                    '$Object:payloadHash': 'payloadHash',
                    '$Object:objectType': 'objectType',
                    '$Object:homomorphicHash': 'homomorphicHash',
                    '$Object:version': 'version'}

VERB_FILTER_DEP = {
                    '$Object:objectID': ['GET', 'HEAD', 'DELETE', 'RANGE', 'RANGEHASH'],
                    '$Object:containerID': ['GET', 'PUT', 'HEAD', 'DELETE', 'SEARCH', 'RANGE', 'RANGEHASH'],
                    '$Object:ownerID': ['GET', 'HEAD'],
                    '$Object:creationEpoch': ['GET', 'PUT', 'HEAD'],
                    '$Object:payloadLength': ['GET', 'PUT', 'HEAD'],
                    '$Object:payloadHash': ['GET', 'PUT', 'HEAD'],
                    '$Object:objectType': ['GET', 'PUT', 'HEAD'],
                    '$Object:homomorphicHash': ['GET', 'PUT', 'HEAD'],
                    '$Object:version': ['GET', 'PUT', 'HEAD']
                }