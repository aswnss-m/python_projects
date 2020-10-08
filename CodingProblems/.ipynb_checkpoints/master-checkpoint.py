{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#this is the datas that is required in the program\n",
    "\n",
    "array = [0,1,2]\n",
    "a_max = max(array)\n",
    "a_min = min(array)\n",
    "missing = list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#now we get all the numbers that is in between the min and max values in the array\n",
    "\n",
    "for i in range(a_min,a_max):\n",
    "    \n",
    "    #for all positive number\n",
    "    if i > 0:\n",
    "        \n",
    "        #if that positive number does not belong in the array , add it to the missing array\n",
    "        if i not in array:\n",
    "            missing.append(i)\n",
    "        #if there is no missing numbers in between , then we return the next positive integer\n",
    "        else:\n",
    "            missing.append(a_max+1)\n",
    "            \n",
    "    #we are going to skip the negative numbers\n",
    "    else:\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3]\n"
     ]
    }
   ],
   "source": [
    "#we the the lowest possing integer therefore we print the lowest value in the missing array\n",
    "\n",
    "print(mix(missing))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
