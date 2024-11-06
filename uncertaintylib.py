import math

# magnitude of x, returns the exponent for scientific notation
def mag(x): return math.floor(math.log10(abs(x)))

# the number of digits to the left of the decimal point
def left_digits(x): return mag(x) + 1

# round formatting given decimals
def fmt_decimals(x, decimals):
    return "{{:.{}f}}".format(max(decimals, 0)).format(round(x, decimals))

# round formatting given sigfigs
def fmt_sigfigs(x, sigfigs): return fmt_decimals(x, sigfigs - left_digits(x))

# test for Python numeric
def is_pynum(x): return isinstance(x, float) or isinstance(x, int)

# an experimental quantity, with uncertainty and sigfigs
class scinum:
    sigfigs: int
    value: float
    pm: float
    
    def __init__(self, value: float, pm: float, sigfigs: int) -> None:
        self.value = value
        self.pm = abs(pm)
        self.sigfigs = sigfigs
    
    # addition overload; take least decimals
    def __add__(self, other):
        if is_pynum(other): # float represents exact value
            least_decimals = self.decimals()
            new_value = self.value + other
            other_pm = 0.0
        else: # should be scinum
            least_decimals = min(self.decimals(), other.decimals())
            new_value = self.value + other.value
            other_pm = other.pm
        
        new_sigfigs = least_decimals + left_digits(new_value)
        
        return scinum(new_value, self.pm + other_pm, new_sigfigs)
    
    # subtraction overload; take least decimals
    def __sub__(self, other):
        if is_pynum(other): # float represents exact value
            least_decimals = self.decimals()
            new_value = self.value - other
            other_pm = 0.0
        else: # should be scinum
            least_decimals = min(self.decimals(), other.decimals())
            new_value = self.value - other.value
            other_pm = other.pm
        
        new_sigfigs = least_decimals + left_digits(new_value)
        
        return scinum(new_value, self.pm + other_pm, new_sigfigs)
    
    # multiplication overload; take least sigfigs
    def __mul__(self, other):
        if is_pynum(other): # float represents exact value
            # easily convertible to scinum for multiplication
            other = scinum(other, 0.0, self.sigfigs)
        
        self_percent = self.pm / abs(self.value)
        other_percent = other.pm / abs(other.value)
        total_percent = self_percent + other_percent
        total_value = self.value * other.value
        
        return scinum(
            total_value,
            total_percent * total_value,
            min(self.sigfigs, other.sigfigs)
        )
    
    # division overload; take least sigfigs
    def __truediv__(self, other):
        if is_pynum(other): # float represents exact value
            # easily convertible to scinum for multiplication
            other = scinum(other, 0.0, self.sigfigs)
        
        self_percent = self.pm / abs(self.value)
        other_percent = other.pm / abs(other.value)
        total_percent = self_percent + other_percent
        total_value = self.value / other.value

        return scinum(
            total_value,
            total_percent * total_value,
            min(self.sigfigs, other.sigfigs)
        )

    # return absolute uncertainty
    def __str__(self) -> str:
        return f"{fmt_sigfigs(self.value, self.sigfigs)}\u00b1{fmt_sigfigs(self.pm, self.sigfigs)}"

    # return percent uncertainty
    def perc(self) -> str:
        return f"{fmt_sigfigs(self.value, self.sigfigs)}\u00b1{self.pm / self.value * 100}%"

    # convert sigfigs to decimal points
    def decimals(self) -> int:
        return self.sigfigs - left_digits(self.value)
