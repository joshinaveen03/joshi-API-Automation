def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRTaW46cGFzc3dvmQxMjM=",
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",

    }
    return headers
