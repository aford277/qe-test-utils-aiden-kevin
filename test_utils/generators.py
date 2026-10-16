"""Data generators. Every generator accepts an optional `seed` so a failing test can be re-run
with exactly the same data. Use a PRIVATE generator: rng = random.Random(seed)
(never random.seed(...), which would change the global random state for everyone)."""
import random
import string

PRIORITIES = ("Low", "Medium", "High")
STATUSES = ("New", "Passed", "Failed")


def generate_username(prefix="user", length=4, seed=None):
    """Return a username like 'user4821': prefix followed by `length` random digits."""
    # TODO: rng = random.Random(seed); join rng.choice(string.digits) `length` times
    rng = random.Random(seed)
    digits = "".join(rng.choice(string.digits) for _ in range(length))
    return f"{prefix}{digits}"


def generate_usernames(count, seed=None):
    """Return a list of `count` UNIQUE usernames like 'user4821' (count must be 9000 or less)."""
    # TODO: rng + a list + a set `seen`; a while loop until you have `count` unique names
    rng = random.Random(seed)
    names = []
    seen = set()
    while len(names) < count:
        sub_seed = rng.randint(0, 1000000)
        name = generate_username(seed = sub_seed)
        if name not in seen:
            seen.add(name)
            names.append(name)
    return names



def generate_password(length=12, seed=None):
    """Return a random password of exactly `length` characters (assume length >= 4)
    that always contains an uppercase letter, a lowercase letter and a digit.
    FOR TEST DATA ONLY: random is not secure."""
    # TODO: rng; start with one upper, one lower, one digit; fill up with a loop; rng.shuffle; join
    rng = random.Random(seed)
    chars = [
        rng.choice(string.ascii_uppercase),
        rng.choice(string.ascii_lowercase),
        rng.choice(string.digits)
    ]
    all_chars = string.ascii_letters + string.digits
    while len(chars) < length:
        chars.append(rng.choice(all_chars))
    rng.shuffle(chars)
    return "".join(chars)


def generate_test_id(number, prefix="TC", digits=3):
    """Return a zero-padded test ID: generate_test_id(7) -> 'TC-007'."""
    # TODO: str(number), then pad with '0' * (digits - len(text))
    text = str(number)
    return prefix + "-" + "0" * (digits - len(text)) + text


def make_test_case(test_id, name, **options):
    """Return a NEW test-case dict with defaults, overridden/extended by keyword options.

    Defaults: priority 'Medium', status 'New', duration 0.0.
    make_test_case('TC-001', 'Login', priority='High', browser='Chrome') adds/overrides keys.
    """
    # TODO: build the defaults dict, then case.update(options); return case
    pass


def generate_test_cases(count, seed=None):
    """Return `count` test-case dicts with IDs TC-001, TC-002, ... and names 'Test case 1', ...

    priority and status are random picks from PRIORITIES / STATUSES;
    duration is a random value from 0.10 to 5.00 seconds (2 decimals).
    """
    # TODO: rng = random.Random(seed); loop number in range(1, count + 1); reuse generate_test_id and make_test_case
    pass