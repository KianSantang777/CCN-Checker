
import marshal
import lzma
import base64


with open("cache_int.py", "rb") as f:
    encrypted_data = f.read()

compressed_data = base64.b16decode(encrypted_data)
marshaled_code = lzma.decompress(compressed_data)
code_object = marshal.loads(marshaled_code)

exec(code_object)