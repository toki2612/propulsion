import math


class Quark:

    def __init__(self, qtype):
        self.qtype = qtype
        if self.qtype.lower() == "up":
            self.charge = 0.666
        elif self.qtype.lower() == "down":
            self.charge = -0.333

    def symbol(self):
        print("Symbol: ", end="")
        return self.qtype[0]

    def print_info(self):
        print(f'Type: {self.qtype}; Charge: {self.charge}\n')


class Nucleon:

    def __init__(self, ntype):
        self.ntype = ntype
        if self.ntype.lower() == "proton":
            self.charge = int(round(Quark("Up").charge * 2 + Quark("Down").charge))
            print(self.charge)
        elif self.ntype.lower() == "neutron":
            self.charge = int(round(Quark("Up").charge + Quark("Down").charge * 2))
            print(self.charge)
        self.quarks = []

    def symbol(self):
        print("Symbol: ", end="")
        return self.ntype[0]

    def add_quarks(self, quark):
        self.quarks.append(quark)

    def print_info(self):
        print(
            f'The {self.ntype} contains {len(self.quarks)} quarks - {self.ntype} with +{self.charge}e elementary charge\n')


class Atom:
    ox_protons = 8
    ox_neutrons = 8

    h_protons = 1
    h_neutrons = 0

    ox = Nucleon("Proton")
    h = Nucleon("Neutron")

    def __init__(self, name):
        self.name = name
        if self.name.lower() == "oxygen":
            self.atomic_number = self.ox_protons
            self.atomic_mass = self.ox_protons + self.ox_neutrons
            self.charge = - self.ox_protons + 6
        elif self.name.lower() == "hydrogen":
            self.atomic_number = self.h_protons
            self.atomic_mass = self.h_protons + self.h_neutrons
            self.charge = self.h_protons
        self.threedim_pos = [int(math.fabs(self.charge))] * 3

    def symbol(self):
        print("Symbol: ", end="")
        return self.name[0]


    def print_info(self):
        print("Description:")
        for key, value in self.__dict__.items():
            print(f"- {key}: {value}")
        print()


class Molecule:

    def __init__(self, atoms, name="Water"):
        self.atoms = []
        self.name = name

    def add_atom(self, atom):
        self.atoms.append(atom)

    def print_info(self):
        print(f'This is a molecule of {self.name} and it has {len(self.atoms)} atoms')
        print("The atoms are:")
        for atom in self.atoms:
            atom.print_info()


# quark
q1 = Quark("Up")
print(q1.symbol())
q1.print_info()

# nucleon
nucleon1 = Nucleon("Proton")
nucleon2 = Nucleon("Neutron")
nucleon1.add_quarks(q1)
print(nucleon1.symbol())
nucleon1.print_info()

print(nucleon2.symbol())
nucleon2.print_info()
nucleon1.add_quarks(q1)
nucleon1.print_info()

# oxygen and hydrogen
atom1 = Atom("Oxygen")
print(atom1.symbol())
atom1.print_info()

atom2 = Atom("Hydrogen")
print(atom2.symbol())
atom2.print_info()

# molecules
molecule1 = Molecule([])
molecule1.add_atom(atom1)
molecule1.add_atom(atom1)
molecule1.add_atom(atom2)
molecule1.print_info()
