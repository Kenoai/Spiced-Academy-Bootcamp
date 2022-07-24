import pickle
import argparse

# the one im modifying

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--prompt', help='ask for a prompt', action='store_true')
#parser.add_argument('-j', '--jens', help='says hello to jens', action='store_true')
#print('hello')
args, unknown = parser.parse_known_args()

with open('fit_it_real_good.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)

string = input("Enter your string: ")
print()
print('I think this text is from...')
prediction = model.predict([string])

print(prediction)

yes_no = input("Do you want to play again?")
yes_no

while yes_no == 'yes':
    print()
    string = input("Enter your string: ")
    print()
    print('I think this text is from...')
    prediction = model.predict([string])
    print(prediction)
    yes_no = input("Do you want to play again? Press Y for 'yes' and N for 'no'")


else:
    print('Was fun playing, have a good day!')
    pass

#if args.randomrose:
#    print('hello random rose')
#if args.jens:
#    print('hello Jens')