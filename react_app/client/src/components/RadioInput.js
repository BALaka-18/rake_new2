import "./css/RadioInput.css";

const RadioInput = (props) => {
  return (
    <div className="radio-input">
      <form>
        {props.labels.map((label) => {
          return (
            <label
              id={"radio-" + label.id}
              key={label.id}
              onClick={() => props.onChoose(label.id)}
            >
              <input type="radio" name={props.name} />
              <span>{label.value}</span>
            </label>
          );
        })}
      </form>
    </div>
  );
};

export default RadioInput;
