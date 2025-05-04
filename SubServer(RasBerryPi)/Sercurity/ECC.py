from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
'''
Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
'''


class ECC:
    def __init__(self,dev_mode = False):
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()
        self.dev_mode = dev_mode
        self.print_keys()

    def print_keys(self):
        if self.dev_mode == True:
            sk_int = self.private_key.private_numbers().private_value
            pub_nums = self.public_key.public_numbers()
            print(f"\nsk: {hex(sk_int)}")
            print(f"pk.x: {hex(pub_nums.x)}")
            print(f"pk.y: {hex(pub_nums.y)}")

    def generate_signature(self,message):
        signature = self.private_key.sign(message,ec.ECDSA(hashes.SHA256()))
        return signature
    
    def verify_signture(self,signature,message):#pass->None error->error message
        try:
            self.public_key.verify(signature,message,ec.ECDSA(hashes.SHA256()))
            print("\nSignature Pass!")
            return True
        except Exception as e:
            print("\nSignature Error!")
            return False
        
    def generate_session_key_ECDH(self,public_key):
        session_key = self.private_key.exchange(ec.ECDH(),public_key)
        return session_key


if __name__ == "__main__":
    m = b"Hi my name is walker"
    m2 = b"Hi my name is frank"
    IoT_decive = ECC(dev_mode=True)
