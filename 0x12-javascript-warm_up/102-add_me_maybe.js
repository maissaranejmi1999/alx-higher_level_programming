#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};

module.exports = { addMeMaybe };
