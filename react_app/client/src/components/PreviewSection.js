import {
  MDBAnimation,
  MDBBtn,
  MDBCol,
  MDBContainer,
  MDBIcon,
  MDBRow,
  MDBView,
} from "mdbreact";
import React from "react";

const PreviewSection = () => {
  return (
    <MDBView className="preview-section">
      <MDBContainer
        style={{ height: "100%", width: "100%", paddingTop: "10rem" }}
        className="d-flex justify-content-center white-text align-items-center"
      >
        <MDBRow>
          <MDBCol md="6" className="text-center mt-xl-5 mb-5">
            <MDBAnimation type="fadeInUp" delay=".5s">
              <h1 className="rake-title font-weight-bold mt-sm-5">RAKE</h1>
            </MDBAnimation>

            <MDBAnimation type="fadeInUp" delay="1.4s">
              <hr className="hr-violet" />
              <p className="mb-4 rake-info text-justify">
                Rapid Automatic Keyword Extraction (RAKE) is a well-known
                keyword extraction method that uses a list of stopwords and
                phrase delimiters to detect the most relevant words or phrases
                in a piece of text
              </p>
            </MDBAnimation>

            <MDBAnimation type="fadeInUp" delay="2s">
              <a
                href="https://pypi.org/project/rake-new2/"
                rel="noreferrer"
                target="_blank"
              >
                <MDBBtn className="btn-round">
                  <MDBIcon fab icon="python" className="mr-1" size="2x" />
                  View on PyPI
                </MDBBtn>
              </a>
              <a
                href="https://github.com/BALaka-18/rake_new2"
                target="_blank"
                rel="noreferrer"
              >
                <MDBBtn outline className="btn-outline-round" color="white">
                  <MDBIcon fab icon="github" className="mr-1" size="2x" />
                  view on github
                </MDBBtn>
              </a>
            </MDBAnimation>
          </MDBCol>

          <MDBCol md="6" className="text-center text-md-left mt-xl-5 mb-5">
            <MDBAnimation
              className="text-center mb-5 mt-0"
              type="fadeInRight"
              delay="1.6s"
            >
              <MDBIcon
                className="color-violet"
                icon="file-contract"
                size="6x"
              />
            </MDBAnimation>
            <MDBAnimation
              className="text-center mb-5"
              type="fadeInUp"
              delay="2.6s"
            >
              <MDBIcon className="color-violet-d" icon="filter" size="9x" />
            </MDBAnimation>
            <MDBAnimation
              className="text-center"
              type="fadeInDown"
              delay="3.2s"
            >
              <MDBIcon className="color-violet" icon="spell-check" size="6x" />
            </MDBAnimation>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </MDBView>
  );
};

export default PreviewSection;
