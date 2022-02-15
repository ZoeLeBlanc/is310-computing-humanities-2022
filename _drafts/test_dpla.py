from dpla.api import DPLA

# DPLA.new_key("zgleblanc@gmail.com")

dpla = DPLA('1729a98a7b0dff2e7e222b7d66a655ec')

result = dpla.search('cooking')

print(result.items)