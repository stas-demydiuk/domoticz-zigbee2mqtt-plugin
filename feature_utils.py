def get_feature(features, feature_name):
    for item in features:
        if 'name' in item and item['name'] == feature_name:
            return item

    return False

def generate_alias(feature, default_value):
    if 'endpoint' in feature:
        return feature['endpoint']
    else:
        return default_value