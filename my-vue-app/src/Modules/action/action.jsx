import React from 'react';

// Try out react action
const submitData = async (data) => {
  const newUser = {
    userName: data.get("userName"),
    password: data.get("password")
  }
  console.log(newUser)
}

const Action = () => {
  const submitDataByEventListener = async (e) => {
    e.preventDefault()
    const newUser = {
      userName: e.target.userName.value,
      password: e.target.password.value
    }
    setTimeout(() => {
      console.log(newUser)
    }, 1000)
  }

  return (
    <div>
      <form onSubmit={submitDataByEventListener} >
        {/* <form action={submitData}> */}
        <input type='text' name='userName' placeholder='Enter your user name' />
        <input type='password' name='password' placeholder='Enter your password' />
        <button type='submit' >Submit</button>
      </form>


    </div>
  );
};

export default Action;
