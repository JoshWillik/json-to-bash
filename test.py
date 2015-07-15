m = __import__('json-to-bash')

tests = [
    ('testKey', 'TEST_KEY'),
    ('anotherTest', 'ANOTHER_TEST'),
    ('manyWordTest', 'MANY_WORD_TEST'),
    ('thisIsAReallyLongOne', 'THIS_IS_A_REALLY_LONG_ONE')
]

print( 'Key Regex should convert camelCase to BASH_FORMAT properly' )
for original, expected in tests:
    converted = m.bashify_key( original, m.KEY_REGEX )
    try:
        assert converted == expected
        print( "Passed: " + original + " => " + expected )
    except AssertionError:
        print( "Failed: " + original + " => " + converted )
    except Exception as e:
        print( "Failed: " + original + " => " + expected + ": " + str(e) )
