{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6bfbd89d-39c8-4f1c-884a-09afb20c52a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "39211be0-2762-4e65-8d76-35e0a4c68afd",
   "metadata": {},
   "outputs": [],
   "source": [
    "life = lambda coffee=True: \"still functioning\" if coffee else \"segmentation fault\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cb94495d-92ba-4c57-bbd2-9522aa38559c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'still functioning'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "life()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "72ad4e3f-a571-40e8-99d2-13f7939eb0ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'segmentation fault'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "life(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "65f5bf97-94d4-4844-a601-90a0f09bcd03",
   "metadata": {},
   "outputs": [],
   "source": [
    "project_status = lambda stars, docs: \"legendary\" if stars > 1000 and docs else \"works_on_my_machine\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2961fd3e-bade-458b-8b70-2a3b2854ff59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'works_on_my_machine'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "project_status(2500, False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bd0fc967-b394-486e-8d54-86ab9b7ca363",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'legendary'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "project_status(2500, True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
