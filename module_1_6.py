Basement = {"Leela": 76561198218966161, "LuxMan": 76561198064963183, "Zala": 76561198426131399}
print(Basement)
print(Basement.get("Leela"))
print(Basement.get("Ghost"))
Basement["Ghost"] = 76561198972082941
Basement.update({"Bunny": 76561198407751342, "Blite": 76561198972082941})
print(Basement)
del Basement["Bunny"]
print(Basement)
Basement_set = {"Leela": 76561198218966161, "LuxMan": 76561198064963183, "Zala": 76561198426131399, "LuxMan": 76561198064963183, "LuxMan": 76561198064963183, "Zala": 76561198426131399}
print(Basement_set)
Basement_set.update({"Bunny": 76561198407751342, "Blite": 76561198972082941, "Blite": 76561198972082941, "Bunny": 76561198407751342})
print(Basement_set)
del Basement_set["Bunny"]
print(Basement_set)