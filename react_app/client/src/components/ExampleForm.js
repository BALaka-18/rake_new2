import {MDBBox, MDBBtn, MDBCol, MDBContainer, MDBInput, MDBRow} from 'mdbreact';
import React, {Fragment, useEffect, useState} from 'react';
import Select from 'react-select';

import RadioInput from './RadioInput';

const ExampleForm = () => {
    const enums =
    {
        KEEP_HTML: 11,
        DONT_KEEP: 12,
        SHOW_WORDS: 21,
        DONT_SHOW: 22,
        GET_KEYWORDS_ONLY: 31,
        GET_KEYWORDS_SCORES: 32,
        GET_TOP_5_KEYWORDS: 33
    };

    const radio1 = [{ id: enums.KEEP_HTML, value: "Keep Html" }, { id: enums.DONT_KEEP, value: "Don't Keep" }];
    const radio2 = [{ id: enums.SHOW_WORDS, value: 'Show Top 5 most Frequent Words' }, { id: enums.DONT_SHOW, value: "Don't Show" }];
    const selectOptions = [
        { label: 'Get Keywords only', value: enums.GET_KEYWORDS_ONLY },
        { label: 'Get keywords with scores', value: enums.GET_KEYWORDS_SCORES },
        { label: 'Get top 5 keywords', value: enums.GET_TOP_5_KEYWORDS }
    ];

    const [text, setText] = useState('');
    const [keepHtml, setKeepHtml] = useState(enums.KEEP_HTML);
    const [showWords, setShowWords] = useState(enums.SHOW_WORDS);
    const [dropdownSelect, setDropdownSelect] = useState(null);
    const [output, setOutput] = useState({});

    useEffect(() => {
        let id1 = 'radio-' + keepHtml;
        let id2 = 'radio-' + showWords;
        document.getElementById(id1).click();
        document.getElementById(id2).click();
    }, [keepHtml, showWords]);


    const fileUpload = () => {
        document.getElementById('file-input').click();
    }

    const getBody = () => {
        let otherOption;
        if (dropdownSelect == null)
            otherOption = 'null';
        else if (dropdownSelect === enums.GET_KEYWORDS_ONLY)
            otherOption = 'kwrd';
        else if (dropdownSelect === enums.GET_KEYWORDS_SCORES)
            otherOption = 'kwrd_score';
        else if (dropdownSelect === enums.GET_TOP_5_KEYWORDS)
            otherOption = 'top5';
        const body = {
            text: text,
            keepHtml: (keepHtml === enums.KEEP_HTML) ? true : false,
            showTop5Words: (showWords === enums.SHOW_WORDS) ? true : false,
            other: otherOption
        };
        return body;
    }

    const extract = () => {
        fetch('http://localhost:6000/extract', {
            method: "POST",
            body: JSON.stringify(getBody()),
            headers: {
                "Content-type": "application/json"
            }
        }).then((response) => response.json())
            .then((data) => setOutput(data));
    }

    return (
        <MDBContainer className='example-form'>
            <h1 className='mb-3 mt-2 text-center'>Test It Now</h1>
            <MDBRow>
                <MDBCol md='6'>
                    <h3 className='mr-5'>Enter Text</h3>
                    <MDBInput type="textarea"
                        label="Text"
                        rows="4"
                        background
                        onChange={(e) => setText(e.target.value)}
                    />
                </MDBCol>
                <MDBCol md='6'>
                    <h3 className='mr-5'>Or Upload a File</h3>
                    <input id='file-input' type='file' hidden />
                    <MDBInput background disabled label="File" className='mb-3' size="lg" />
                    <MDBBtn className='mt-2' gradient="purple" onClick={() => fileUpload()}>Upload</MDBBtn>
                </MDBCol>
            </MDBRow>
            <MDBRow className='mt-3 justify-content-center'>
                <RadioInput labels={radio1} name='radio1' onChoose={setKeepHtml} />
            </MDBRow>
            <MDBRow className='mt-3 justify-content-center'>
                <RadioInput labels={radio2} name='radio2' onChoose={setShowWords} />
            </MDBRow>

            <MDBRow className='justify-content-center'>
                <Select className='dropdown-select' options={selectOptions} onChange={(dropdown) => setDropdownSelect(dropdown.value)} />
            </MDBRow>
            <MDBRow className='mt-2 justify-content-center'>
                <MDBBtn gradient='purple' onClick={() => extract()}>Extract</MDBBtn>
            </MDBRow>
            <MDBBox className='output'>
                {output.top5Words ? <Fragment>
                    <strong>Top 5 Most Frequent Words :</strong>
                    <br />
                    {Object.keys(output.top5Words).map((key, index) => <p>{key} = {output.top5Words[key]}</p>)}
                </Fragment> : <></>}
                {output.keyword_scores ?
                    <Fragment>
                        <strong>Keyword Scores :</strong>
                        <br />
                        {output.keyword_scores.map((item) =>
                            <Fragment> <p>{item[1]} = {item[0]}</p></Fragment>
                        )}
                    </Fragment>
                    :
                    <></>
                }
                {output.keywords ?
                    <Fragment>
                        <strong> Keywords : </strong>
                        <br />
                        {output.keywords.map((item) => <span>{item}, </span>)}
                    </Fragment> : <> </>
                }

            </MDBBox>
        </MDBContainer >
    )
}

export default ExampleForm;