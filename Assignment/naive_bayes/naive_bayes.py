import naive_bayes_train
import naive_bayes_test

def main():
    print "Calling train in train"
    execfile('naive_bayes_train.py')
    print "calling test"
    execfile('naive_bayes_test.py')

main()
