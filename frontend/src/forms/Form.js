// import logo from './logo.svg';
import '../App.css';

function Form() {
    return (
      <div className="Form">
        <form>
            <label for="cheese">Do you like cheese?</label>
            <input type="checkbox" name="cheese" id="cheese"/> 
            <input type='button' value='Submit'/>
        </form>
      </div>
    );
  }
  
  export default Form;